import numpy as np 
import os
import matplotlib.pyplot as plt

scaling_list = np.linspace(0.82,1.05,231)

similarity_pcc = []
similarity_scc = []
similarity_sis = []
#CHNO
with open('nist_id.dat','r') as f:
    lines = f.readlines()
nist_id = [line.strip() for line in lines]
for nist in nist_id:
    if os.path.exists(f'specific_scaling/{nist}/pcc.npy'):
        similarity_pcc.append(np.load(f'specific_scaling/{nist}/pcc.npy'))
        similarity_scc.append(np.load(f'specific_scaling/{nist}/scc.npy'))
        similarity_sis.append(np.load(f'specific_scaling/{nist}/sis.npy'))

#FClBr
with open('nist_id_FClBr.dat','r') as f:
    lines = f.readlines()
nist_id = [line.strip() for line in lines]
for nist in nist_id:
    if os.path.exists(f'specific_scaling/{nist}/pcc.npy'):
        similarity_pcc.append(np.load(f'specific_scaling/{nist}/pcc.npy'))
        similarity_scc.append(np.load(f'specific_scaling/{nist}/scc.npy'))
        similarity_sis.append(np.load(f'specific_scaling/{nist}/sis.npy'))

#SiPS
with open('nist_id_SiPS.dat','r') as f:
    lines = f.readlines()
nist_id = [line.strip() for line in lines]
for nist in nist_id:
    if os.path.exists(f'specific_scaling/{nist}/pcc.npy'):
        similarity_pcc.append(np.load(f'specific_scaling/{nist}/pcc.npy'))
        similarity_scc.append(np.load(f'specific_scaling/{nist}/scc.npy'))
        similarity_sis.append(np.load(f'specific_scaling/{nist}/sis.npy'))


similarity_pcc = np.array(similarity_pcc)
similarity_scc = np.array(similarity_scc)
similarity_sis = np.array(similarity_sis)
avg_pcc = np.array([np.mean(each) for each in similarity_pcc.T])
avg_scc = np.array([np.mean(each) for each in similarity_scc.T])
avg_sis = np.array([np.mean(each) for each in similarity_sis.T])
print(f'Maximum PCC: {max(avg_pcc)}')
print(f'Fitting to PCC')
opt_idx_pcc = avg_pcc.argsort()[-1]
print(f'Optimal scaling factor: {opt_idx_pcc*0.001+0.82}')
print(f'Averaged PCC: {avg_pcc[opt_idx_pcc]}')
print(f'Averaged SCC: {avg_scc[opt_idx_pcc]}')
print(f'Averaged SIS: {avg_sis[opt_idx_pcc]}')
print(f'Averaged PCC (unscaled): {avg_pcc[180]}')
print(f'Averaged SCC (unscaled): {avg_scc[180]}')
print(f'Averaged SIS (unscaled): {avg_sis[180]}')

print(f'Maximum SCC: {max(avg_scc)}')
print(f'Fitting to SCC')
opt_idx_scc = avg_scc.argsort()[-1]
print(f'Optimal scaling factor: {opt_idx_scc*0.001+0.82}')
print(f'Averaged PCC: {avg_pcc[opt_idx_scc]}')
print(f'Averaged SCC: {avg_scc[opt_idx_scc]}')
print(f'Averaged SIS: {avg_sis[opt_idx_scc]}')

print(f'Maximum SIS: {max(avg_sis)}')
print(f'Fitting to SIS')
opt_idx_sis = avg_sis.argsort()[-1]
print(f'Optimal scaling factor: {opt_idx_sis*0.001+0.82}')
print(f'Averaged PCC: {avg_pcc[opt_idx_sis]}')
print(f'Averaged SCC: {avg_scc[opt_idx_sis]}')
print(f'Averaged SIS: {avg_sis[opt_idx_sis]}')