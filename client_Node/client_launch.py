import os
def launcher(data):
    x=os.getcwd()
    y=x[x.find('UE_4'):]
    z=y[:y.find(os.sep)]
    g=r"{}".format(x[:x.find('UE_4')])+z+r"\Engine\Binaries\Win64\UE4Editor-Cmd.exe"
    frame_list=[]
    print(data["jobs"])
    for i in data["jobs"]:
        print(i)
        frame_list.append([int(i["custom_start_frame"]),int(i["custom_end_frame"])])

    command=['"{}" '.format(g),
        r'"{}" '.format(data["jobs"][0]["project_dir"]),
        r'-game ' ,
        r'-MoviePipelineLocalExecutorClass=/Script/MovieRenderPipelineCore.MoviePipelinePythonHostExecutor ',
        r'-ExecutorPythonClass=/Engine/PythonTypes.MoviePipelineExampleRuntimeExecutor ',
        r'-asset_path={} '.format(data["jobs"][0]["asset_path"]),
        r'-custom_frames="{}" '.format(frame_list),
        r'-log']
    s=""
    for i in command:
        s=s+i
    print(s)
    os.system('cmd /k "{}"'.format(s))