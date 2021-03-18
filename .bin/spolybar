#!/bin/bash

# ----------------------------------------------
# Descritpion : Polybar style changer
# Autor : Berthose Fin (birkhoff)
# Date : 2021-02-13
# ----------------------------------------------

DIR="$HOME/.config/polybar"
STYLE=$(sed -n '4s/STYLE=//p' $DIR/launch.sh);

if [[ "$1" == "default" ]]; then
	style="default"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "blocks" ]]; then
	style="blocks"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "cuts" ]]; then
	style="cuts"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "docky" ]]; then
	style="docky"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "fin" ]]; then
	style="fin"
	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "forest" ]]; then
	style="forest"
   	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "grayblocks" ]]; then
	style="grayblocks"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "hack" ]]; then
	style="hack"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "material" ]]; then
	style="material"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "minimal" ]]; then
	style="minimal"
    	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "topy" ]]; then
	style="topy"
	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

elif [[ "$1" == "wave" ]]; then
	style="wave"
	sed -i "s/$STYLE/$1/g" $DIR/launch.sh
	sh $DIR/launch.sh

else
	cat <<- EOF
	
	Spolybar - polybar style changer

	Usage:
	spolybar [THEME]
		
	Available Themes :
	. default	. blocks	. cuts
	. docky		. fin		. forest	
	. grayblocks	. hack		. material	
	. minimal	. topy		. wave

	EOF
fi
