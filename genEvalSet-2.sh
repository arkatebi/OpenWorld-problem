date
python xTract_reevalSet -I1=evalSet-1.mfo.map -I2=uniprot_sprot.dat.2012_01 -N=F -O=evalSet-2
echo 'DONE'
date 
python xTract_reevalSet -I1=evalSet-1.bpo.map -I2=uniprot_sprot.dat.2012_01 -N=P -O=evalSet-2
echo 'DONE'
date
python xTract_reevalSet -I1=evalSet-1.cco.map -I2=uniprot_sprot.dat.2012_01 -N=C -O=evalSet-2
date
