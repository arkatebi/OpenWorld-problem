date
python xTract_reevalSet -I1=evalSet-5.mfo.1.map -I2=uniprot_sprot.dat.2016_01 -N=F -O=evalSet-6
echo 'DONE'
date 
python xTract_reevalSet -I1=evalSet-5.bpo.1.map -I2=uniprot_sprot.dat.2016_01 -N=P -O=evalSet-6
echo 'DONE'
date
python xTract_reevalSet -I1=evalSet-5.cco.1.map -I2=uniprot_sprot.dat.2016_01 -N=C -O=evalSet-6
date
