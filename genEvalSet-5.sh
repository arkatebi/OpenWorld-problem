date
python xTract_reevalSet -I1=evalSet-4.mfo.1.map -I2=uniprot_sprot.dat.2015_01 -N=F -O=evalSet-5
echo 'DONE'
date 
python xTract_reevalSet -I1=evalSet-4.bpo.1.map -I2=uniprot_sprot.dat.2015_01 -N=P -O=evalSet-5
echo 'DONE'
date
python xTract_reevalSet -I1=evalSet-4.cco.1.map -I2=uniprot_sprot.dat.2015_01 -N=C -O=evalSet-5
date
