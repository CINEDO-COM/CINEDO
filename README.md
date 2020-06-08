**CINEDO**

**Οδηγίες προβολής**

Προαπαιτούμενα: 
• Λειτουργικό σύστημα που να υποστηρίζει εκδόσεις Python3.6+ ()

Για να μπορέσετε να τρέξετε τον κώδικα και να ελέγξετε τις επιμέρους λειτουργίες του, θα χρειαστεί να γίνει εγκατάσταστη των εξής: 
• Εκδοση pip 18.01 και άνω 
• Virtual Environment 
• Django Framework

---

**Windows**

   1. Δημιουργήστε ένα φάκελο όπου θέλετε να αποθηκεύσετε τα αρχεία του προγράμματος, κατεβάστε τον κώδικα από το github και αποθηκεύστε το στο συγκεκριμένο φάκελο
   2. Αφού έχετε κατεβάσει την τελευταία edition της Python, ανοίξτε κάποιο terminal (εμείς χρησιμοποιήσαμε το Git Bash)
   3. Ανοίξτε το terminal σας και Εκτελέστε την εντολή cd /c/"name of your directory"
   4. Εκτελέστε την εντολή python -m venv virtual
   5. Για να ενεργοποιήσετε το virtual environment εκτελέστε source virtual/scripts/activate
   6. Με ενεργοποιημένο το virtual environment, εγκαταστήστε το Django εκτελώντας την εντολή pip install django
   7. Εκτελέστε pip freeze για να ελέγξετε εάν έχει εγκατασταθεί το django
   8. Εκτελέστε επίσης την εντολή python -m pip install Pillow
   9. Αφού εγκατασταθεί το Django εκτελέστε την εντολή python manage.py runserver
  10.  Aνοίξτε τον browser σας και γραψτε στη γραμμη διευθύνσεων localhost:8000
  11.  Πλέον έχετε πρόσβαση στην εφαρμογή και μπορείτε να περιηγηθείτε ελεύθερα

---

**MAC OS**

   1. Δημιουργήστε ένα φάκελο όπου θέλετε να αποθηκεύσετε τα αρχεία του προγράμματος, κατεβάστε τον κώδικα από το github και αποθηκεύστε το στο συγκεκριμένο φάκελο
   2. Ανοίξτε τη γραμμή εντολών (command prompt)
   3. Εκτελέστε την εντολή curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   4. Εκτελέστε την εντολή python get-pip.py
   5. Πηγαίνετε στον φάκελο όπου θέλετε να τρέξετε το πρόγραμμα με την εντολή cd /path/to/directory
   6. Εκτελέστε την εντολή python3.8 -m pip install pipenv
   7. Εκτελέστε την εντολή pipenv
   8. Εκτελέστε την εντολή mkdir Dev
   9. Εκτελέστε την εντολή mkdir ~/Dev/cfehome
  10. cd ~/Dev/cfehome
  11. pipenv install --python 3.8
  12. Μέσα από το φάκελο ενεργοποιήστε το virtual environment εκτελώντας την εντολή pipenv shell
  13. Με ενεργοποιημένο το virtual environment, εγκαταστήστε το Django εκτελώντας την εντολή pipenv install Django
  14. Εκτελέστε επίσης την εντολή python -m pip install Pillow
  15. Αφού εγκατασταθεί το Django εκτελέστε την εντολή python manage.py runserver
  16. Aνοίξτε τον browser σας και γραψτε στη γραμμη διευθύνσεων localhost:8000
  17. Πλέον έχετε πρόσβαση στην εφαρμογή και μπορείτε να περιηγηθείτε ελεύθερα

---

**Linux**

   1. Δημιουργήστε ένα φάκελο όπου θέλετε να αποθηκεύσετε τα αρχεία του προγράμματος, κατεβάστε τον κώδικα από το github και αποθηκεύστε το στο συγκεκριμένο φάκελο
   2. Ανοίξτε τη γραμμή εντολών (command prompt)
   3. Εκτελέστε την εντολή
      Ubuntu 
        ◦ sudo apt install python-pip #εγκατάσταση pip για python2 
        ◦ sudo apt install python3-pip #εγκατάσταση pip για python3
      CentOS & RHEL 
        • yum install epel-release 
        • yum install python-pip
      Fedora 
        ◦ dnf install python-pip #εγκατάσταση pip για python2 
        ◦ dnf install python3 #εγκατάσταση pip για python3
      Arch Linux 
        ◦ pacman -S python2-pip #εγκατάσταση pip για python2 
        ◦ pacman -S python-pip #εγκατάσταση pip για python3
      openSUSE 
        • zypper install python-pip #εγκατάσταση pip για python2 
        • zypper install python-pip #εγκατάσταση pip για python3
    4. Πηγαίνετε στον φάκελο όπου θέλετε να τρέξετε το πρόγραμμα με την εντολή cd /path/to/directory
    5. Εκτελέστε την εντολή python3 -m venv env #εγκατάσταση virtual environment, το υπογραμισμένο αλλάζει ανάλογα με το χρήστη και το πως θέλει να ονομαστεί ο αντίστοιχος φάκελος
    6. Μέσα από το φάκελο ενεργοποιήστε το virtual environment εκτελώντας την εντολή source ./env/bin/activate #το υπογραμισμένο αλλάζει ανάλογα με το πως το ονόμασε ο χρήστης κατά την εγκατάσταση
    7. Με ενεργοποιημένο το virtual environment, εγκαταστήστε το Django εκτελώντας την εντολή pip install Django ή pip3 install Django
    8. Εκτελέστε επίσης την εντολή pip install pillow
    9. Αφού εγκατασταθεί το Django εκτελέστε την εντολή python manage.py runserver
   10. Aνοίξτε τον browser σας και γραψτε στη γραμμη διευθύνσεων localhost:8000
   11. Πλέον έχετε πρόσβαση στην εφαρμογή και μπορείτε να περιηγηθείτε ελεύθερα

---

**Κωδικοί χρηστών**

Για απλούς χρήστες, πηγαίνετε στη σελίδα "localhost:8000/accounts/login" και συνδέεστε με τα παρακάτω στοιχεία:

  username: test2
  password: 123456

--Διαφορετικά μπορείτε να εγγραφείτε με δικά σας στοιχεία μέσω της σελίδας "localhost:8000/accounts/register"


Για διαχειριστές, πηγαίνετε στη σελίδα "localhost:8000/admin" και συνδέεστε με τα παρακάτω στοιχεία:

  username: cinedo-admin
  password: 123456

--Διαφορετικά μπορείτε να δημιουργήσετε δικό σας λογαριασμό διαχειριστή με δικά σας στοιχεία τρέχοντας στο τέρμιναλ την εντολή "python manage.py createsuperuser" (πάντα μέσα από το directory του project (είναι αυτό όπου βρίσκεται το αρχείο manage.py) και με ενεργοποιημένο το virtual environment)
