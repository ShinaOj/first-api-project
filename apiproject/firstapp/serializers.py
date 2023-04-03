from rest_framework import serializers
from .models import Students




class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Students
        # fields=['id', 'firstName', 'lastname', 'email', 'phonenumber', 'address', 'gender']
        fields= '__all__'
        read_only_fields= ['id']
                









class StudentSerializer(serializers.Serializer):
    gender_choice=(
        ('male', 'Male'),
        ('female', 'Female')
    )
    firstName= serializers.CharField(required=True, max_length=100)
    lastname= serializers.CharField(required=True, max_length=100)
    email=serializers.EmailField(required=True, max_length=100)
    address=serializers.CharField(required=True, max_length=100)
    phonenumber=serializers.CharField(required=True, max_length=14)
    gender=serializers.ChoiceField(choices=gender_choice)



    def validate(self, attrs):
        return super().validate(attrs)
    

    def create(self, validated_data):
        # do any custom logic
        student= Students.objects.create(**validated_data)
        return student
    
    def update(self, instance, validated_data):
        instance.firstName=validated_data.get('firstName', instance.firstName)
        instance.lastname=validated_data.get('lastname', instance.lastname)
        instance.email=validated_data.get('email', instance.email)
        instance.address=validated_data.get('address', instance.address)
        instance.gender=validated_data.get('gender', instance.gender)
        instance.save()
        return instance
