for i in $(ls);
do 
	if grep -q pass $i 
	then
 	   	echo $i
		echo found string 'pass'
	fi
done
