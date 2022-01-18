#!/bin/bash --login

text=$(mktemp)
cat <<'EOF' >"$text"

case "$OSTYPE" in

    darwin*) 
        export CONDA_DIR=${HOME}/opt/anaconda3
        ;;

    *) 
        export CONDA_DIR=${HOME}/anaconda3
        ;;
esac

export PATH=$CONDA_DIR/bin:$PATH

cd $HOME
source activate pelagos

EOF

/bin/bash --init-file <(cat $text)


