PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as invitees:
    invitee_list = invitees.readlines()
with open('./Input/Letters/starting_letter.txt') as template_file:
    template = template_file.read()

for invitee in invitee_list:
    # removing the new line from the name's list
    invitee = invitee.strip()
    # OR
    # invitee=invitee.replace('\n', '')

    # replacing the name in the template file
    ready_file = template.replace(PLACEHOLDER, invitee)

    # writing the new invite as a new file in the specified location
    with open(f"./Output/ReadyToSend/letter_for_{invitee}.txt", mode='w') as ready_invite:
        ready_invite.write(ready_file)
