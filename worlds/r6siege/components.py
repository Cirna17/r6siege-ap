from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .client.launch import launch_rainbow_six_siege_text_client
    
    launch(launch_rainbow_six_siege_text_client, name="Rainbow Six Siege Client", args=args)
    
components.append(
    Component(
        "Rainbow Six Siege Client",
        func = run_client,
        game_name = "Rainbow Six Siege",
        component_type = Type.CLIENT,
        supports_uri = False
    )
)