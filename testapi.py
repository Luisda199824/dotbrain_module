from dotbrain_module import *

api_key = '3C7H0T'
api_key_secret = 'D19BCL08UM87C8CYNWQ5'
token='1WPLOS'
ordering_by='blank'
value='5'
base='5'
numeric='true'
user='blank'
weigth_key='blank'
email='Luisda199824@gmail.com'
name='Prueba de creación conferencia API'
normal_mean=False
printInfo=True
key='11'
weigth='10'

'''sendAnswerd(
    api_key=api_key,
    api_key_secret=api_key_secret,
    token=token,
    value=value,
    base=base,
    numeric=numeric,
    user=user,
    weigth_key=weigth_key,
    printInfo=True
)

getServiceBasicInfo(
    api_key=api_key,
    api_key_secret=api_key_secret,
    token=token,
    printInfo=True
)

data = setQuestionKey(
    api_key=api_key,
    api_key_secret=api_key_secret,
    token=token,
    key=key,
    weigth=weigth,
    printInfo=False
)

data = create_conference(
    api_key=api_key,
    api_key_secret=api_key_secret,
    name=name,
    email=email,
    normal_mean=normal_mean,
    printInfo=False
)'''

data = get_info_service(
    api_key=api_key,
    api_key_secret=api_key_secret,
    token=token,
    ordering_by=ordering_by,
    get_answers='y', 
    printInfo=False
)

print(data)