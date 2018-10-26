import cgi, cgitb, os, sys, codecs
import st05.main

def main():
    cgitb.enable()
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

    q = cgi.FieldStorage()
    self_url = os.environ['SCRIPT_NAME']
    st05.main.main(q, self_url)

main()