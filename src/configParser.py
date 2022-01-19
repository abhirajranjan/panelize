import typing
import configparser
import pathlib


def readCfg(cfgfile: typing.Union[str, pathlib.Path]) -> dict:
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    
    if type(cfgfile) == str:
        cfgfile = pathlib.Path(cfgfile)
    if not cfgfile.exists():
        raise FileNotFoundError(f'config file {cfgfile} does not exists')
    
    with open(cfgfile) as cfgf:
        config.read_file(cfgf)
    
    return config