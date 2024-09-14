#!/bin/bash

time=$(date +%Y-%m-%d-%H-%M-%S)
dir="$(xdg-user-dir PICTURES)/Screenshots"
file="Screenshot_${time}_${RANDOM}.png"

# Notification et visualisation de la capture d'écran
notify_view() {
  notify-send -h string:x-canonical-private-synchronous:shot-notify -u normal "Screenshot"
  viewnior "${dir}/$file"
}

# Décompte avant la capture
countdown() {
  for sec in $(seq "$1" -1 1); do
    notify-send -h string:x-canonical-private-synchronous:shot-notify -t 1000 "Taking shot in: $sec"
    sleep 1
  done
}

# Fonction pour les captures d'écran
shotnow() {
  scrot -F "${dir}/$file"
  notify_view
}

shot5() {
  countdown 5
  sleep 0.5 && shotnow
}

shot10() {
  countdown 10
  sleep 0.5 && shotnow
}

shotwin() {
  scrot -u -F "${dir}/$file"
  notify_view
}

shotarea() {
  scrot -s -F "${dir}/$file"
  notify_view
}

# Création du répertoire de captures d'écran s'il n'existe pas
if [[ ! -d "$dir" ]]; then
  mkdir -p "$dir"
fi

# Sélection de l'option en fonction du paramètre fourni
case "$1" in
--now)
  shotnow
  ;;
--in5)
  shot5
  ;;
--in10)
  shot10
  ;;
--win)
  shotwin
  ;;
--area)
  shotarea
  ;;
*)
  echo -e "Available Options: --now --in5 --in10 --win --area"
  ;;
esac

exit 0
