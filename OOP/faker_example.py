
from faker import Faker

fake = Faker("pl_Pl")
print(fake.name())
print(fake.text(15))

print(dir(fake))