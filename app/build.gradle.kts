plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.example.a3_1module_3handson2"
    compileSdk {
        version = release(36)
    }

    defaultConfig {
        applicationId = "com.example.a3_1module_3handson2"
        minSdk = 24
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    kotlinOptions {
        jvmTarget = "11"
    }
}

dependencies {

    // AndroidX Core
    implementation("androidx.core:core-ktx:1.17.0")

    // AppCompat
    implementation("androidx.appcompat:appcompat:1.7.1")

    // Material Design
    implementation("com.google.android.material:material:1.13.0")

    // ConstraintLayout
    implementation("androidx.constraintlayout:constraintlayout:2.2.1")

    // RecyclerView
    implementation("androidx.recyclerview:recyclerview:1.4.0")

    // Retrofit
    implementation("com.squareup.retrofit2:retrofit:2.11.0")

    // Gson converter for Retrofit
    implementation("com.squareup.retrofit2:converter-gson:2.11.0")

    // Kotlin Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")

    // Lifecycle + lifecycleScope
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.9.2")
}