# Postgresql & Archlinux

## Install

```sh
sudo pacman -S postgresql
```

## Init

```sh
sudo -u postgres -i initdb -D /var/lib/postgres/data
```

## Start service

```sh
sudo systemctl start postgresql
```

## Create admin user

```sh
sudo su - postgres
psql
```

```psql
sudo su - postgres
psql
```
