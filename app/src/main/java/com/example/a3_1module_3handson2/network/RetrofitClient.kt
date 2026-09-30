package com.example.a3_1module_3handson2.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitClient {

    // Android Emulator -> Flask running on your PC
    private const val BASE_URL =
        "http://10.0.2.2:5000/"

    val apiService: ApiService by lazy {

        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(
                GsonConverterFactory.create()
            )
            .build()
            .create(ApiService::class.java)
    }
}