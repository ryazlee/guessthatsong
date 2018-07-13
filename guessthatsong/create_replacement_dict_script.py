def create_replacement_dict(data):
  replacement_dict = {}
  lines = data.split("\n")
  for line in lines:
    word, emoji, _ = line.split(":")
    replacement_dict[word] = emoji
  return replacement_dict

data = ' I: <i class="em em-eye"></i>:\none:<i class="em em-one"></i>:\n1:<i class="em em-one"></i>:\ntwo:<i class="em em-two"></i>:'

print("Data used:\n" + data)
print("Dict created:\n" + str(create_replacement_dict(data)))
