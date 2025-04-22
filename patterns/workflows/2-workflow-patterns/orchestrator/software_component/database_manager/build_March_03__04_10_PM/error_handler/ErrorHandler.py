using System;
using System.IO;

namespace ErrorHandlerModule
{
    public interface IErrorLogging
    {
        void LogError(string message, Exception exception);
        void DisplayUserFeedback(string message);
    }

    public class ErrorHandler : IErrorLogging
    {
        private readonly string logFilePath;

        public ErrorHandler(string logFilePath)
        {
            this.logFilePath = logFilePath;
        }

        public void LogError(string message, Exception exception)
        {
            string logMessage = $"[{DateTime.Now}] - ERROR: {message} - Exception: {exception.Message}\nDetails: {exception.StackTrace}";
            File.AppendAllText(logFilePath, logMessage + "\n");
        }

        public void DisplayUserFeedback(string message)
        {
            // In a real application, this could be a dialog box or a logging system.
            Console.WriteLine(message);
        }
    }
}