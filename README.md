# verify-pot
step 1: find the run, subruns from the final wirecell checkout
make sure the # of events in the checkout is close enough to the number of events from reco2

step 2: find the run, subruns from the reco2 metadata
subruns that has been completed removed by the beam filter will still show up in the metadata, but not in artroot

bash script: samweb-run-subrun.sh
usage: 
	samweb list-files "defname: <reco2 def>" > run_subrun.txt
	nohup ./samweb-run-subrun.sh run_subrun.txt > run_subrun.out &

step 3: find the subruns with corrupted metadata

command:
	samweb list-files --summary "file_type data and file_format binary% and data_tier raw and run_number>=4952 and run_number<=6998 and file_name PhysicsRun% and start_time<2015-01-01'" > run_subrun.txt  # can also try 1971-01-01 as the corrupted metadata is 1970-01-01
	nohup ./samweb-run-subrun.sh run_subrun.txt > run_subrun.out &

        === run3
        samweb list-files "file_type data and file_format binary% and data_tier raw and ( (run_number>=13697 and run_number<=18062) or (run_number>=18202 and run_number<=18960) ) and file_name PhysicsRun% and start_time<'2000-01-01'"


step 4:	summarize "missing" pot with the information obtained above

script: verify-pot-run[1,2,3].py

=== run number range
Run1 C1: 4952-6998
Run2 D1,D2,E1: 8317-11951
Run3 F,G1,G2G2a: 13697-18062, 18202-18960


=== reco2 definition (07.01.2021)
wcp_union_reco2_data_bnb_run1_C1_noBeamFilterFor5312-5367_mcc9_v08_00_00_51_reco2_reco2

wcp_union_reco2_data_bnb_run2_D1_mcc9_v08_00_00_51_reco2_reco2
wcp_union_reco2_data_bnb_run2_D2_mcc9_v08_00_00_51_reco2_reco2
wcp_union_reco2_data_bnb_run2_E1_mcc9_v08_00_00_51_reco2_reco2

wcp_union_reco2_data_bnb_run3_F_mcc9_v08_00_00_51_reco2_reco2
wcp_union_reco2_data_bnb_run3_G1_mcc9_v08_00_00_51_reco2_reco2
wcp_unified_reco2_data_bnb_run3_G2_mcc9_v08_00_00_51_reco2_reco2
wcp_unified_reco2_data_bnb_run3_G2a_mcc9_v08_00_00_51_reco2_reco2

