from configparser import ConfigParser
import os
import tests
from orastorage.model import Identity

# def save_ini_file(base_dir, filename, config_obj):
#     if not os.path.exists(base_dir) or not os.path.isdir(base_dir):
#         raise IOError("Directory({}) is not exist.".format(base_dir))
#     file_path = base_dir + '/' + filename
#     config_file = open(file_path, 'w')
#     config_obj.write(config_file)
#     config_file.close()
#
#
# def read_ini_file(base_dir, filename):
#     if not os.path.exists(base_dir) or not os.path.isdir(base_dir):
#         raise IOError("Directory({}) is not exist.".format(base_dir))
#
#     filepath = base_dir + '/' + filename
#     if not os.path.exists(filepath):
#         f = open(filepath, 'w')
#         f.close()
#
#     ini = ConfigParser()
#     ini.read(filepath)
#     return ini


def get_target_dir_for_test():
    target_dir = os.path.dirname(tests.__file__) + "/../target"
    if not os.path.exists(target_dir):
        os.mkdir(target_dir, 0o755)

    return os.path.abspath(target_dir)


def get_login_info():
    basedir = get_target_dir_for_test()
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    filename = "cache_orastorage.ini"
    filepath = basedir + "/" + filename

    if not os.path.exists(filepath):
        user_id = os.environ.get("ORASTORAGE_ID")
        password = os.environ.get("ORASTORAGE_PASSWORD")
        identity_domain = os.environ.get("ORASTORAGE_DOMAIN")

        if id is None or password is None or identity_domain is None:
            msg = "Environment Variables are not exist. (ORASTORAGE_ID={}, ORASTORAGE_PASSWORD={}, ORASTORAGE_DOMAIN{}"
            raise EnvironmentError(msg.format(id, password, identity_domain))

        section = 'login'
        login_info = ConfigParser()
        login_info.add_section(section)
        login_info.set(section, 'user_id', user_id)
        login_info.set(section, 'password', password)
        login_info.set(section, 'identity_domain', identity_domain)

        config_file = open(filepath, 'w')
        login_info.write(config_file)
        config_file.close()
    else:
        login_info = ConfigParser()
        login_info.read(filepath)

    return login_info


def remove_login_info():
    basedir = get_target_dir_for_test()
    filename = "cache_orastorage.ini"
    file_path = basedir + "/" + filename

    if os.path.exists(file_path):
        os.remove(file_path)


def get_identity():
    login_ini = get_login_info()
    identity = Identity(login_ini.get('login', 'identity_domain'),
                       login_ini.get('login', 'user_id'),
                       login_ini.get('login', 'password'))
    return identity

