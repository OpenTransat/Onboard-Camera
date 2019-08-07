lastnum=`ls -v *.$1 2>/dev/null | grep -E '[0-9]+\.'$1'$' | tail -n 1 | cut -f1 -d\.`
echo $lastnum
