from single_name import SingleName

country_name = SingleName("rwanda")

print(country_name)
print(country_name.response_data().official)
print(country_name.response_data().currency)
print(country_name.response_data().capital)
print(country_name.response_data().subregion)
print(country_name.response_data().language)
print(country_name.response_data().landlocked)
print(country_name.response_data().car)
print(country_name.response_data().continent)
