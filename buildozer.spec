[app]

# (str) Title of your application
title = Medicine Scanner

# (str) Package name
package.name = medicine_scanner

# (str) Package domain (use reverse domain notation)
package.domain = org.yourname

# (str) Application version
version = 1.0.0

# (str) Application requirements
# Specify all libraries and dependencies here, separate them with commas.
# You can also add any additional libraries you need for your app.
requirements = python3,kivy,opencv-python,pytesseract,googletrans==4.0.0rc1

# (int) Application version code
version.code = 1

# (str) Custom source folders for your own custom classes
#source.include_dirs =

# (list) Application icons
# Add the path to your app's icon here (if you have one).
# icon.filename = %(source.dir)s/icon.png

# (list) Application dependencies
# Uncomment to include extra dependencies (like Pillow, OpenCV, etc.)
#requirements = python3,kivy,pillow,opencv-python,pytesseract,googletrans==4.0.0rc1

# (str) Build type (debug/release)
# Debug builds are the default option. For release, use the `release` type.
buildozer = debug

# (bool) Whether or not to include an Android debug key
# In release, you would need a proper key to sign your app.
#debug = True

# (str) Android package name
# Uncomment and edit the following line to set a custom package name
#android.package = com.example.mymedicineapp
