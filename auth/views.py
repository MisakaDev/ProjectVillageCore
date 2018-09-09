from rest_auth.views import LoginView


class Login(LoginView):
    def get_response(self):
        response = super().get_response()
        response.data['id'] = self.user.id
        response.data['username'] = self.user.username
        return response
