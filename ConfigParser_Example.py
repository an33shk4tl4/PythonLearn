import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

def read_config_file():
    print str(cfg)
    print cfg['english']
    print cfg['french']
    print cfg['french']['greeting']
    print cfg['files']['bin']

if __name__ == '__main__':
    read_config_file()

