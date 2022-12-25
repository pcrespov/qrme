import json
import sys
from getpass import getpass
from pathlib import Path

import segno
from segno import QRCode, helpers

CURRENT_DIR = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent
ASSETS_DIR = CURRENT_DIR.parent / "assets"


def create_wifi_qcode(ssid: str, password: str) -> None:
    qrcode: QRCode = helpers.make_wifi(
        ssid=ssid, password=password, security="WPA", hidden=False
    )
    outfile = f"{ssid.replace(' ', '_')}.qr.png"
    qrcode.save(outfile, scale=2)


def create_vcard_qcode():
    data = json.loads(Path("vcard.json").read_text())
    vcard = helpers.make_vcard_data(**data)

    filename = data["displayname"].replace(" ", "_")
    Path(f"{filename}.vcard").write_text(vcard)

    qrcode = segno.make(vcard, error="H")
    outfile = f"{filename}.qr.png"
    qrcode.save(outfile)


def create_url_qcodes():
    for name, url in [
        ("demo1", "https://pcrespov.github.io/qrme/"),
        ("ytb_losgallardos", "https://youtu.be/ToriXXzdrqM"),
        ("ytb_tijola", "https://youtu.be/sMcGpewYT6Q"),
        ("ytb_mojacar", "https://youtu.be/sshzFr8bnow"),
        ("ytb_vera_80v", "https://youtu.be/YQZKpu6Nofo"),
        *zip(
            "web facebook youtube linkedin".split(),
            (
                "http://www.s1ngular.es/",
                "https://www.facebook.com/ingenierias1NGular/",
                "https://www.youtube.com/channel/UCh2u4MCFwSwHNANTmbWy2nw",
                "https://es.linkedin.com/in/alejandro-crespo-valero-2b764a35",
            ),
        ),
    ]:
        qrcode = segno.make(url)
        # standard version
        qrcode.save(f"{name}.qr.pdf")
        # artistic version
        qrcode.to_artistic(
            background=f"{ASSETS_DIR}/s1ng-avatar.jpg",
            target=f"{name}.art.qr.pdf",
            scale=10,
        )


def create_url_invitation(code: str):
    name = "osparc"
    qrcode = segno.make(
        f"https://osparc.io/#/registration/?invitation={code}",
        error="h",
    )
    qrcode.save(f"{name}.qr.pdf")
    qrcode.to_artistic(
        background=f"{ASSETS_DIR}/osparc-black.png",
        target=f"{name}.art.qr.pdf",
        scale=10,
    )


if __name__ == "__main__":

    # s1ngular
    create_url_qcodes()
    # create_vcard_qcode()
    # rene
    # create_wifi_qcode(ssid=input("WIFI SSID:"), password=getpass())
    # osparc
    # create_url_invitation(code="1234")
