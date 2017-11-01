import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

print str(cfg)

print cfg['english']

print cfg['french']

print cfg['french']['greeting']

print cfg['files']['bin']



