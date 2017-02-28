import ConfigParser
import os
import tests


def save_ini_file(base_dir, filename, config_obj):
    if not os.path.exists(base_dir) or not os.path.isdir(base_dir):
        raise IOError("Directory({1}) is not exist.".format(base_dir))
    file = base_dir+'/'+filename
    config_file = open(file, 'w')
    config_obj.write(config_file)
    config_file.close()

def read_ini_file(base_dir, filename):
    if not os.path.exists(base_dir) or not os.path.isdir(base_dir):
        raise IOError("Directory({}) is not exist.".format(base_dir))

    filepath = base_dir+'/'+filename
    if not os.path.exists(filepath):
        print 'file not found'
        f = open(filepath, 'w')
        f.close()

    ini = ConfigParser.ConfigParser()
    ini.read(filepath)
    return ini



def get_data_dir_for_test():
    return '{}{}{}'.format(os.path.dirname(tests.__file__),"/","data")


def get_login_info():
    basedir = get_data_dir_for_test()
    filename = "cache_orastorage.ini"
    filepath = basedir+"/"+filename

    if not os.path.exists(filepath):
        id = os.environ.get("ORASTORAGE_ID")
        password = os.environ.get("ORASTORAGE_PASSWORD")
        identity_domain = os.environ.get("ORASTORAGE_DOMAIN")

        if id is None or password is None or identity_domain is None:
            msg = "Environment Variables arn't exist. (ORASTORAGE_ID={}, ORASTORAGE_PASSWORD={}, ORASTORAGE_DOMAIN{}"
            raise EnvironmentError(msg.format(id, password, identity_domain))

        section = 'login'
        login_info = ConfigParser.ConfigParser()
        login_info.add_section(section)
        login_info.set(section, 'id', id)
        login_info.set(section, 'password', password)
        login_info.set(section, 'identity_domain', identity_domain)

        config_file = open(filepath, 'w')
        login_info.write(config_file)
        config_file.close()
    else:
        login_info = ConfigParser.ConfigParser()
        login_info.read(filepath)

    return login_info

def remove_login_info():
    basedir = get_data_dir_for_test()
    filename = "cache_orastorage.ini"
    filepath = basedir+"/"+filename

    if os.path.exists(filepath):
        os.remove(filepath)






