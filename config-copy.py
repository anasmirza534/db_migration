#!/usr/bin/python3

mysql = {
    "source": {
        "username"  : "username",
        "password"  : "password",
        "backup_dir": "./mysql_backup"
    },
    "destination": {
        "username"  : "username",
        "password"  : "password",
        "backup_dir": "./mysql_backup"
    }
}

mongo = {
    "source": {
        "username"  : "username",
        "password"  : "password",
        "backup_dir": "./mongo_backup"
    },
    "destination": {
        "username"  : "username",
        "password"  : "password",
        "backup_dir": "./mongo_backup"
    }
}

config = {
    "mysql": mysql, "mongo": mongo
}
