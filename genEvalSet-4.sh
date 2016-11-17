date
python xTract_reevalSet -I1=evalSet-3.mfo.1.map -I2=uniprot_sprot.dat.2014_01 -N=F -O=evalSet-4
echo 'DONE'
date 
python xTract_reevalSet -I1=evalSet-3.bpo.1.map -I2=uniprot_sprot.dat.2014_01 -N=P -O=evalSet-4
echo 'DONE'
date
python xTract_reevalSet -I1=evalSet-3.cco.1.map -I2=uniprot_sprot.dat.2014_01 -N=C -O=evalSet-4
date
