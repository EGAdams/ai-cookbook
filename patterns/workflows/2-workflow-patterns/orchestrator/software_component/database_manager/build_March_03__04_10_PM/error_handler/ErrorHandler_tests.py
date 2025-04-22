using System;
using System.IO;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace ErrorHandlerModule.Tests
{
    [TestClass]
    public class ErrorHandlerTests
    {
        private const string LogFilePath = "testLog.txt";

        [TestInitialize]
        public void Initialize()
        {
            if (File.Exists(LogFilePath))
                File.Delete(LogFilePath);
        }

        [TestMethod]
        public void LogError_ShouldWriteErrorToLog()
        {
            var errorHandler = new ErrorHandler(LogFilePath);
            var exception = new Exception("Test exception");

            errorHandler.LogError("An error occurred", exception);

            var logContents = File.ReadAllText(LogFilePath);
            Assert.IsTrue(logContents.Contains("ERROR: An error occurred"));
            Assert.IsTrue(logContents.Contains("Test exception"));
        }

        [TestMethod]
        public void DisplayUserFeedback_ShouldPrintMessage()
        {
            using (var sw = new StringWriter())
            {
                Console.SetOut(sw);
                var errorHandler = new ErrorHandler(LogFilePath);
                errorHandler.DisplayUserFeedback("User feedback message");

                var result = sw.ToString().Trim();
                Assert.AreEqual("User feedback message", result);
            }
        }
    }
}