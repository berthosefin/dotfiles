import { User } from "@prisma/client";
import { NextApiRequest, NextApiResponse } from "next";
import { updateUser, getUserById, deleteUser } from "@/lib/prisma/users";
