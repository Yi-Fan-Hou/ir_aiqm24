import mlatom as ml 
import numpy as np 
import os 
import matplotlib.pyplot as plt

if not os.path.exists('specific_scaling'):
    os.mkdir('specific_scaling')

scaling_list = np.linspace(0.82,1.05,231)

# CHNO
with open('nist_id.dat','r') as f:
    lines = f.readlines()
nist_id = [line.strip() for line in lines]

for nist in nist_id[:1]:
    print(nist)
    if not os.path.exists(f'specific_scaling/{nist}'):
        os.mkdir(f'specific_scaling/{nist}')
    if not os.path.exists(f'specific_scaling/{nist}/unnormalized_ir.npy'):
        data = []
        similarity_pcc = []
        similarity_scc = []
        similarity_sis = []
        if not os.path.exists(f'../static/data/{nist}/ir.npy'): continue
        exp = np.load(f'../../experiments/data/{nist}/exp.npy')
        aiqm1 = np.load(f'../static/data/{nist}/ir.npy')
        if len(aiqm1[0]) == 0: continue
        # spec_exp = ml.data.spectrum(raw_data=exp.T)
        spec_exp = ml.spectra.spectrum(x=exp[0],y=exp[1])
        spec_exp.normalize('average')
        for scaling in scaling_list:
            aiqm1_copy = np.copy(aiqm1)
            aiqm1_copy[0] = aiqm1_copy[0] * scaling
            # spec_aiqm1 = ml.data.spectrum(raw_data=aiqm1_copy.T).broaden(xlist=exp[0],broadening_function_type='Lorentzian',broadening_function_kwargs={'w':30}) # fwhm=30 cm^-1
            spec_aiqm1 = ml.spectra.spectrum.broaden(line_spectrum=aiqm1_copy.T,spectrum_range=exp[0],broadening_func='Lorentzian',broadening_func_kwargs={'w':30}) # fwhm=30 cm^-1
            # Save unnormalized spectrum
            data.append(spec_aiqm1.y)

            spec_aiqm1.normalize('average')

            similarity_pcc.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='PCC',line_up=False))
            similarity_scc.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='SCC',line_up=False))
            similarity_sis.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='SIS',line_up=False))

        np.save(f'specific_scaling/{nist}/unnormalized_ir.npy',data)
        np.save(f'specific_scaling/{nist}/pcc.npy',similarity_pcc)
        np.save(f'specific_scaling/{nist}/scc.npy',similarity_scc)
        np.save(f'specific_scaling/{nist}/sis.npy',similarity_sis)

# FClBr
with open('nist_id_FClBr.dat','r') as f:
    lines = f.readlines()
nist_id = [line.strip() for line in lines]

for nist in nist_id[:1]:
    print(nist)
    if not os.path.exists(f'specific_scaling/{nist}'):
        os.mkdir(f'specific_scaling/{nist}')
    if not os.path.exists(f'specific_scaling/{nist}/unnormalized_ir.npy'):
        data = []
        similarity_pcc = []
        similarity_scc = []
        similarity_sis = []
        if not os.path.exists(f'../static_FClBr/data/{nist}/ir.npy'): continue
        exp = np.load(f'../../experiments/data/{nist}/exp.npy')
        aiqm1 = np.load(f'../static_FClBr/data/{nist}/ir.npy')
        if len(aiqm1[0]) == 0: continue
        # spec_exp = ml.data.spectrum(raw_data=exp.T)
        spec_exp = ml.spectra.spectrum(x=exp[0],y=exp[1])
        spec_exp.normalize('average')
        for scaling in scaling_list:
            aiqm1_copy = np.copy(aiqm1)
            aiqm1_copy[0] = aiqm1_copy[0] * scaling
            # spec_aiqm1 = ml.data.spectrum(raw_data=aiqm1_copy.T).broaden(xlist=exp[0],broadening_function_type='Lorentzian',broadening_function_kwargs={'w':30}) # fwhm=30 cm^-1
            spec_aiqm1 = ml.spectra.spectrum.broaden(line_spectrum=aiqm1_copy.T,spectrum_range=exp[0],broadening_func='Lorentzian',broadening_func_kwargs={'w':30}) # fwhm=30 cm^-1
            # Save unnormalized spectrum
            data.append(spec_aiqm1.y)

            spec_aiqm1.normalize('average')

            similarity_pcc.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='PCC',line_up=False))
            similarity_scc.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='SCC',line_up=False))
            similarity_sis.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='SIS',line_up=False))

        np.save(f'specific_scaling/{nist}/unnormalized_ir.npy',data)
        np.save(f'specific_scaling/{nist}/pcc.npy',similarity_pcc)
        np.save(f'specific_scaling/{nist}/scc.npy',similarity_scc)
        np.save(f'specific_scaling/{nist}/sis.npy',similarity_sis)

# SiPS
with open('nist_id_SiPS.dat','r') as f:
    lines = f.readlines()
nist_id = [line.strip() for line in lines]

for nist in nist_id[:1]:
    print(nist)
    if not os.path.exists(f'specific_scaling/{nist}'):
        os.mkdir(f'specific_scaling/{nist}')
    if not os.path.exists(f'specific_scaling/{nist}/unnormalized_ir.npy'):
        data = []
        similarity_pcc = []
        similarity_scc = []
        similarity_sis = []
        if not os.path.exists(f'../static_SiPS/data/{nist}/ir.npy'): continue
        exp = np.load(f'../../experiments/data/{nist}/exp.npy')
        aiqm1 = np.load(f'../static_SiPS/data/{nist}/ir.npy')
        if len(aiqm1[0]) == 0: continue
        # spec_exp = ml.data.spectrum(raw_data=exp.T)
        spec_exp = ml.spectra.spectrum(x=exp[0],y=exp[1])
        spec_exp.normalize('average')
        for scaling in scaling_list:
            aiqm1_copy = np.copy(aiqm1)
            aiqm1_copy[0] = aiqm1_copy[0] * scaling
            # spec_aiqm1 = ml.data.spectrum(raw_data=aiqm1_copy.T).broaden(xlist=exp[0],broadening_function_type='Lorentzian',broadening_function_kwargs={'w':30}) # fwhm=30 cm^-1
            spec_aiqm1 = ml.spectra.spectrum.broaden(line_spectrum=aiqm1_copy.T,spectrum_range=exp[0],broadening_func='Lorentzian',broadening_func_kwargs={'w':30}) # fwhm=30 cm^-1
            # Save unnormalized spectrum
            data.append(spec_aiqm1.y)

            spec_aiqm1.normalize('average')

            similarity_pcc.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='PCC',line_up=False))
            similarity_scc.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='SCC',line_up=False))
            similarity_sis.append(ml.spectra.spectrum_comparison.spectrum_comparison(spec_exp,spec_aiqm1,metric='SIS',line_up=False))

        np.save(f'specific_scaling/{nist}/unnormalized_ir.npy',data)
        np.save(f'specific_scaling/{nist}/pcc.npy',similarity_pcc)
        np.save(f'specific_scaling/{nist}/scc.npy',similarity_scc)
        np.save(f'specific_scaling/{nist}/sis.npy',similarity_sis)
