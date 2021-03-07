import os

if not os.path.exists('WAMSbin_conversion_folder'):
    os.mkdir('WAMSbin_conversion_folder')
    input('Put the files in the folder')
if not os.path.exists('WAMSbin_output'):
    os.mkdir('WAMSbin_output')

for x in os.listdir('WAMSbin_conversion_folder'):
    name, extent = x.split('.', 2)

    with open('WAMSbin_conversion_folder\\' + x, 'rb')as convert:
        cbin = convert.readlines()
        convert.close()
    with open('WAMSbin_output\\' + name + ' & ' + extent + '.WAMSbin', 'wb')as convert:
        convert.writelines(cbin)
        convert.close()