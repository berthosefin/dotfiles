import clientPromise from "@/lib/mongodb";
import type { NextApiRequest, NextApiResponse } from 'next'

export default async (req: NextApiRequest, res: NextApiResponse) => {
    try {
        const client = await clientPromise
        const db = client.db("posts")
        const {title, content} = req.body
    }
}