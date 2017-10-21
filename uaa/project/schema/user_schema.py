from project import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email', 'created_at')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
