#!/usr/bin/env bash

# Fonction pour obtenir toutes les sorties d'affichage actives
get_active_displays() {
    xrandr | grep " connected" | awk '{print $1}'
}

# Exécution de xidlehook avec gestion des écrans multiples
xidlehook \
  `# Ne pas verrouiller si une application est en plein écran` \
  --not-when-fullscreen \
  `# Ne pas verrouiller s'il y a du son en cours` \
  --not-when-audio \
  `# Diminuer la luminosité de tous les écrans après 150 secondes, restaurer si l'utilisateur devient actif` \
  --timer 150 \
  'for display in $(get_active_displays); do xrandr --output "$display" --brightness .1; done' \
  'for display in $(get_active_displays); do xrandr --output "$display" --brightness 1; done' \
  `# Verrouiller l'écran et restaurer la luminosité après 300 secondes supplémentaires` \
  --timer 300 \
  'for display in $(get_active_displays); do xrandr --output "$display" --brightness 1; done; sh ~/.config/i3/scripts/lock.sh' \
  '' \
  `# Éteindre les écrans après 330 secondes de plus` \
  --timer 330 \
  'xset dpms force off' \
  'xset dpms force on' \
  `# Suspendre le système après 1800 secondes supplémentaires` \
  --timer 1800 \
  'systemctl suspend' \
  ''
