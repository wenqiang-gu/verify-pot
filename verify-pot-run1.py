#!/usr/bin/env python
from ROOT import *

run_subrun_ntuple=[]
f1 = TFile.Open("/pnfs/uboone/persistent/users/wirecell/checkout/nearsideband/data_bnb_run1_C1_wirecell_checkout_rootfile_merged_filter_eLEE_near.root")
t = f1.Get("wcpselection/T_pot")
# t.Show(0)
for entry in t:
    rs = (t.runNo, t.subRunNo)
    run_subrun_ntuple.append(rs)
f1.Close()

run_subrun_reco2=[]
with open('wc_reco2_run1_C1.out') as f2:
# with open('run-subrun-pelee-only.txt') as f2:
    for line in f2:
        c = line.strip('\n').split()
        run = int(c[2])
        subrun = int(c[3])
        # run = int(c[0])
        # subrun = int(c[1])
        run_subrun_reco2.append( (run, subrun) ) 

# find the missing subruns in checkout but exist in reco2
set_reco2 = set(run_subrun_reco2)
set_ntuple = set(run_subrun_ntuple)
set_miss = set_reco2 - set_ntuple


run_subrun_falsemeta=[]
with open('wgu_run1_c1_falsemeta.out') as f3:
    for line in f3:
        c = line.strip('\n').split()
        run = int(c[2])
        subrun = int(c[3])
        run_subrun_falsemeta.append( (run, subrun) )

set_falsemeta = set(run_subrun_falsemeta)
set_miss_goodmeta = set_miss - set_falsemeta
set_miss_badmeta = set_miss.intersection(set_falsemeta)
print("(reco2) %d (checkout) %d (miss) %d (miss_goodmeta) %d (miss_badmeta) %d" %(len(set_reco2), len(set_ntuple), len(set_miss), len(set_miss_goodmeta), len(set_miss_badmeta)))


set_chkout_badmeta = set_ntuple.intersection(set_falsemeta)
print("overlap subruns for checkout vs. bad metadata: %d" %len(set_chkout_badmeta))
# for rs in set_chkout_badmeta:
#    print("%d %d" %(rs[0], rs[1]))
  

for rs in set_reco2:
    print("%d %d" %(rs[0], rs[1]))

with open('runsubrun_miss_goodmeta.out','w') as fmiss_goodmeta:
  for rs in set_miss_goodmeta:
    fmiss_goodmeta.write("%d %d\n" %(rs[0], rs[1]))
  

with open('runsubrun_miss_badmeta.out','w') as fmiss_badmeta:
  for rs in set_miss_badmeta:
    fmiss_badmeta.write("%d %d\n" %(rs[0], rs[1]))
