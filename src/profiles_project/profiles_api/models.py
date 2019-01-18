from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """

    Helps Django with the custom user model.

    """

    def create_user(self, email, name, password=None):

        """

        Creates a new user profile object.

        """

        if not email:
            raise ValueError('Users mmust have an email address.')

        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db) # self._db represents the model in which is being used, in this case if we use the class "UserProfileManager" inside *
        # * UserProfile then self._db will refer as to the model UserProfile and the info will be saved inside it

        return user



    def create_superuser(self, email, name, password):
        
        """    

        Creates and saves a new super user

        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):

    """
    
    Respents a "user profile" inside our system.

    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()


    USERNAME_FIELD = 'email' # USERNAME_FIELD is already a REQUIRED_FIELD by default
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):

        """

        Used to get a users full name.

        """

        return self.name

    def get_short_name(self):

        """

        Used to get a users short name.

        """
        
        return self.name

    def __str__(self):

        """

        Convert object into string.

        """

        return self.email

