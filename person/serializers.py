from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	highlight = serializers.HyperlinkedIdentityField(view_name="person-detail", format="html")
	class Meta:
		model = Person
		fields =( 
			"url",
			"guid",
			"highlight",
			"firstName",
			"lastName",
			"middleName",
			"birthDate",
			"gender",
        )
		

