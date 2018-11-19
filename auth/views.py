from rest_auth.views import LoginView


class Login(LoginView):
    def get_response(self):
        response = super().get_response()
        response.data['id'] = self.user.id
        response.data['username'] = self.user.username
        response.data['permission'] = [perm.name for perm in self.user.user_permissions.all()]
        return response
