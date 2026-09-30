package com.example.a3_1module_3handson2.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

import androidx.recyclerview.widget.RecyclerView

import com.example.a3_1module_3handson2.R
import com.example.a3_1module_3handson2.model.DocumentResult

class SearchAdapter(
    private var documents: List<DocumentResult> = emptyList()
) : RecyclerView.Adapter<SearchAdapter.DocumentViewHolder>() {

    inner class DocumentViewHolder(
        itemView: View
    ) : RecyclerView.ViewHolder(itemView) {

        private val titleTextView: TextView =
            itemView.findViewById(
                R.id.tvDocumentTitle
            )

        private val similarityTextView: TextView =
            itemView.findViewById(
                R.id.tvSimilarity
            )

        private val contentTextView: TextView =
            itemView.findViewById(
                R.id.tvDocumentContent
            )

        fun bind(document: DocumentResult) {

            titleTextView.text =
                document.title

            similarityTextView.text =
                "Similarity: ${
                    String.format(
                        "%.4f",
                        document.similarity
                    )
                }"

            contentTextView.text =
                document.content
        }
    }

    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): DocumentViewHolder {

        val view = LayoutInflater.from(
            parent.context
        ).inflate(
            R.layout.item_document,
            parent,
            false
        )

        return DocumentViewHolder(view)
    }

    override fun onBindViewHolder(
        holder: DocumentViewHolder,
        position: Int
    ) {

        holder.bind(
            documents[position]
        )
    }

    override fun getItemCount(): Int {
        return documents.size
    }

    fun updateDocuments(
        newDocuments: List<DocumentResult>
    ) {

        documents = newDocuments

        notifyDataSetChanged()
    }

    fun clearDocuments() {

        documents = emptyList()

        notifyDataSetChanged()
    }
}