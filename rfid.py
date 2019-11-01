# from pirc522 import RFID
# rdr = RFID()
import main
def ovscan():
    try:
        while True:
            ovNummer = input('Kies een random OVnummer')
            try:
                ovNummer = int(ovNummer)
                if ovNummer < 0:
                    print('Kies een positief getal')
                    continue
                elif main.kluisCheck(ovNummer)[1]:
                    print("U kunt niet twee kluisjes beheren op een OV")
                    continue
                else:
                    print(ovNummer)
                    return ovNummer
            except:
                print("Kies een getal bestaande alleen uit cijfers.")
                continue
          # rdr.wait_for_tag()
          # (error, tag_type) = rdr.request()
          # if not error:
          #   print("Tag detected")
          #   (error, uid) = rdr.anticoll()
          #   if not error:
          #     print("UID: " + str(uid))
          #     # Select Tag is required before Auth
          #     if not rdr.select_tag(uid):
          #       # Auth for block 10 (block 2 of sector 2) using default shipping key A
          #       if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
          #         # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
          #         print("Reading block 10: " + str(rdr.read(10)))
          #         # Always stop crypto1 when done working
          #         rdr.stop_crypto()
    except:
        print("an error occured")
    finally:
        pass
        # rdr.cleanup()
    # Calls GPIO cleanup
    # rdr.cleanup()