import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";
import { send } from "vite";

const ddbClient = new DynamoDBClient({ region: "us-east-1" });

const sendToDynamoDB = async () => {
    const params = {
        TableName: 'pokemon-ratings',
        Key: {
             'id': {S : '123'}, 'name': { S:'John Doe'}
        },
    }
    try {
        const data = await ddbClient.send(new GetItemCommand(params));
        console.log('Record created successfully:', data);
    } catch (error) {
        console.error('Error creating record:', error);
    }
}

sendToDynamoDB()