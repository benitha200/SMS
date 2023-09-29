from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import authenticate
from rest_framework import exceptions
from xml.dom import minidom

class UrlAuthentication(BaseAuthentication):
    """
    HTTP Url authentication against username/password.
    """
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        
        userid=None
        password=None
        
        if ('text/xml' in request.content_type.split(';')) or ('application/xml' in request.content_type.split(';')):
            return None
        
        if request.method == 'POST':
            if 'username' in request.POST.keys():
                if 'password' in request.POST.keys():
                    userid=str(request.POST['username'])
                    password=str(request.POST['password'])
                else:
                    msg = 'Missing Password Parameter'
                    raise exceptions.AuthenticationFailed(msg)
            else:
                msg = 'Missing Username Parameter'
                raise exceptions.AuthenticationFailed(msg)
            
        if request.method == 'GET':
            if 'username' in request.GET.keys():
                if 'password' in request.GET.keys():
                    userid=str(request.GET.get('username'))
                    password=str(request.GET.get('password'))
                else:
                    msg = 'Missing Password Parameter'
                    raise exceptions.AuthenticationFailed(msg)
            else:
                msg = 'Missing Username Parameter'
                raise exceptions.AuthenticationFailed(msg)
            
    
        return self.authenticate_credentials(userid, password)
    
    def authenticate_credentials(self, userid, password):
        """
        Authenticate the userid and password against username and password.
        """
        user = authenticate(username=userid, password=password)
        if user is None or not user.is_active:
            raise exceptions.AuthenticationFailed('Invalid username/password')
        return (user, None)

    def authenticate_header(self, request):
        
        return 'URL realm="%s"' % self.www_authenticate_realm
    
class WSDLAuthentication(BaseAuthentication):
    """
    HTTP WSDL authentication against username/password.
    """
    www_authenticate_realm = 'xml'

    def authenticate(self, request):
        
        try:
            userid=None
            password=None
            root=None
            header=None
            soapheader=None
            
            body=request.body
            dom = minidom.parseString(body)
            
            if dom.childNodes:
                if dom.childNodes[0].localName=='Envelope':
                    root=dom.childNodes[0]
                else:
                    msg = 'Missing Envelope Item'
                    raise exceptions.AuthenticationFailed(msg)
                    
            for item in root.childNodes:
                if item.localName=='Header':
                    header=item
            
            if header==None:
                msg = 'Missing Header Item'
                raise exceptions.AuthenticationFailed(msg)
            else:
                for item in header.childNodes:
                    if item.localName=='RequestSOAPHeader':
                        soapheader=item
            
            if soapheader==None:
                msg = 'Missing RequestSOAPHeader Item'
                raise exceptions.AuthenticationFailed(msg)
            else:
                for item in soapheader.childNodes:
                    if item.localName=='username':
                        userid=item.childNodes[0].data 
                    elif item.localName=='password':
                        password=item.childNodes[0].data
                    
            if userid==None:
                msg = 'Missing Username Parameter'
                raise exceptions.AuthenticationFailed(msg)
            elif password==None:
                msg = 'Missing Password Parameter'
                raise exceptions.AuthenticationFailed(msg)
        except:
            msg = 'Invalid Request'
            raise exceptions.AuthenticationFailed(msg)       
        
        return self.authenticate_credentials(userid, password)
    
    def authenticate_credentials(self, userid, password):
        """
        Authenticate the userid and password against username and password.
        """
        user = authenticate(username=userid, password=password)
        if user is None or not user.is_active:
            raise exceptions.AuthenticationFailed('Invalid username/password')
        return (user, None)
    
    def authenticate_header(self, request):
        
        return 'WSDL realm="%s"' % self.www_authenticate_realm