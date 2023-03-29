def checker(args0):
    import torch, os
    from pathlib import Path
    p = Path.cwd().joinpath('weights')
    a = os.listdir(p)
    model_list = ["char0.pt", "tent0.pt"]
    link = {
        'char0.pt':'https://download1073.mediafire.com/l31l9xarfkag1uiVWl6NKZJ4RTgoJpTtdTXW4fKsfYNlLWWDNUBUHF_TdT87TC-GGZt0P0uwxU7RCrFdOddHOrFYM9GUOhA/1n47lkxxf5mecmf/char0.pt%22id=%22downloadButton',
        'tent0.pt':'https://download1522.mediafire.com/csxld8c57hpgzml8zDajt8sxXEqQLuOxnxherHluixpHaGyGTnP_O7eEV3DbuAWn6IgoJH31Zw4r4u47NVtRXozbgCFnxbk/7kx4u7jmvujkksa/tent0.pt"id="downloadButton' }
    if args0 in model_list:
        if args0 not in a:
            torch.hub.download_url_to_file(link[args0], p.joinpath(args0), progress=True)
def ch(args0):
    import torch, os
    from pathlib import Path
    p = Path.cwd().joinpath('weights')
    a = os.listdir(p)
    model_list = ["char0.pt", "tent0.pt"]
    link = {
        'char0.pt':'https://download1073.mediafire.com/l31l9xarfkag1uiVWl6NKZJ4RTgoJpTtdTXW4fKsfYNlLWWDNUBUHF_TdT87TC-GGZt0P0uwxU7RCrFdOddHOrFYM9GUOhA/1n47lkxxf5mecmf/char0.pt%22id=%22downloadButton',
        'tent0.pt':'https://download1522.mediafire.com/csxld8c57hpgzml8zDajt8sxXEqQLuOxnxherHluixpHaGyGTnP_O7eEV3DbuAWn6IgoJH31Zw4r4u47NVtRXozbgCFnxbk/7kx4u7jmvujkksa/tent0.pt"id="downloadButton' }
    if args0 in model_list:
        if args0 not in a:
            torch.hub.download_url_to_file(link[args0], p.joinpath(args0), progress=True)