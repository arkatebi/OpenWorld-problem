date
python xTract_reevalSet -I1=evalSet-2.mfo.1.map -I2=uniprot_sprot.dat.2013_01 -N=F -O=evalSet-3
echo 'DONE'
date 
python xTract_reevalSet -I1=evalSet-2.bpo.1.map -I2=uniprot_sprot.dat.2013_01 -N=P -O=evalSet-3
echo 'DONE'
date
python xTract_reevalSet -I1=evalSet-2.cco.1.map -I2=uniprot_sprot.dat.2013_01 -N=C -O=evalSet-3
date
