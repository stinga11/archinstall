from typing import override

from archinstall.default_profiles.profile import DisplayServerType, GreeterType, Profile, ProfileType


class BudgieProfile(Profile):
	def __init__(self) -> None:
		super().__init__(
			'Budgie',
			ProfileType.DesktopEnv,
			support_gfx_driver=True,
			display_server=DisplayServerType.Wayland,
		)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'materia-gtk-theme',
			'budgie',
			'papirus-icon-theme',
			'gnome-terminal',
			'nemo',
			'nemo-fileroller',
			'rhythmbox',
			'gthumb',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.LightdmSlick
